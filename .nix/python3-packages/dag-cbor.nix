{
  lib,
  fetchPypi,
  buildPythonPackage,
  setuptools,
  setuptools-scm,
  typing-extensions,
  typing-validation,
  multiformats,
}:
buildPythonPackage rec {
  pname = "dag-cbor";
  version = "0.3.2";
  format = "pyproject";

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-0RMFDW9ctsGjJMkRaExdqjBUJXAlhVcyab7zAAqp8QY=";
  };

  propagatedBuildInputs = [
    setuptools
    setuptools-scm
    typing-extensions
    typing-validation
    multiformats
  ];
}
