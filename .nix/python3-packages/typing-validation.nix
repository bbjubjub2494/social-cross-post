{
  lib,
  fetchPypi,
  buildPythonPackage,
  poetry-core,
  setuptools,
}:
buildPythonPackage rec {
  pname = "typing-validation";
  version = "1.0.0";
  format = "pyproject";

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-5jF5uPmL2gKWwSGkqtnZ//avdM28dGazx6B1Ka6VexE=";
  };

  postPatch = ''
    sed -i '/\s*multiformats/d' setup.cfg # break circular dependency
  '';

  propagatedBuildInputs = [
    poetry-core
    setuptools
  ];
}
