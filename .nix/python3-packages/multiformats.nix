{
  lib,
  fetchPypi,
  buildPythonPackage,
  setuptools-scm,
  poetry-core,
  setuptools,
  multiformats-config,
  typing-validation,
  bases,
  typing-extensions,
}:
buildPythonPackage rec {
  pname = "multiformats";
  version = "0.2.1";
  format = "pyproject";

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-Su5utSicPNADFePyuX42tg22r5vOyR1l8y1xVZQtvvk=";
  };

  nativeBuildInputs = [
    setuptools-scm
  ];

  propagatedBuildInputs = [
    poetry-core
    setuptools
    multiformats-config
    typing-validation
    bases
    typing-extensions
  ];
}
