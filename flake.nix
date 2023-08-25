{
  description = "Description for the project";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = inputs @ {
    self,
    flake-parts,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} {
      imports = [
        inputs.flake-parts.flakeModules.easyOverlay
      ];

      systems = ["x86_64-linux"];
      perSystem = {
        self',
        inputs',
        final,
        pkgs,
        system,
        ...
      }: let
        python3Packages = pkgs.python3Packages.override {
          overrides = final': prev':
            builtins.mapAttrs (_: p: final'.callPackage p {}) (self.lib.collectFlat .nix/python3-packages);
        };
      in {
        legacyPackages = {inherit python3Packages;};

        packages = rec {
          social-cross-post-python-module = python3Packages.social-cross-post;
          default = social-cross-post-python-module;
        };

        formatter = final.alejandra;
      };
      flake = {
        # The usual flake attributes can be defined here, including system-
        # agnostic ones like nixosModule and system-enumerating ones, although
        # those are more easily expressed in perSystem.
        lib = let
          collectGen = doRec: dir:
            with inputs.nixpkgs.lib;
              if !builtins.pathExists dir
              then {}
              else
                mapAttrs'
                (name: type: let
                  parsedName = builtins.match "(.*)\\.nix" name;
                in
                  if type == "regular" && parsedName != null
                  then nameValuePair (builtins.head parsedName) (dir + "/${name}")
                  else if type == "directory" && builtins.pathExists (dir + "/${name}/default.nix")
                  then nameValuePair name (dir + "/${name}")
                  else if type == "directory" && doRec
                  then nameValuePair name (collectGen doRec (dir + "/${name}"))
                  else throw "${dir}/${name}: expected a nix file or directory")
                (builtins.readDir dir);
        in {
          collectFlat = collectGen false;
          collectRec = collectGen true;
        };
      };
    };
}
