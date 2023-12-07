{
  lib,
  fetchPypi,
  buildPythonPackage,
  poetry-core,
  setuptools,
  setuptools-scm,
}:
buildPythonPackage rec {
  pname = "multiformats-config";
  version = "0.2.0";
  format = "pyproject";

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-+GiNtPnFm7GvwoK1Q/H+qCT/RxzzZc2GpfQYvZJ2X+0=";
  };

  postPatch = ''
    sed -i '/\s*multiformats/d' setup.cfg # break circular dependency
  '';

  nativeBuildInputs = [ setuptools-scm ];

  propagatedBuildInputs = [
    poetry-core
    setuptools
  ];
}
