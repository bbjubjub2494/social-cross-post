{
  lib,
  fetchPypi,
  poetry-core,
  setuptools,
  setuptools-scm,
  typing-validation,
  typing-extensions,
  buildPythonPackage,
}:
buildPythonPackage rec {
  pname = "bases";
  version = "0.2.1";
  format = "pyproject";

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-sJmeFHJbWb/ziXSwDpGGKeDinz2ApA4CLG8PjVzf+dQ=";
  };

  nativeBuildInputs = [ setuptools-scm ];

  propagatedBuildInputs = [
    poetry-core
    setuptools
    typing-validation
    typing-extensions
  ];
}
