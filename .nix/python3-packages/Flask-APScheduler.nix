{
  lib,
  fetchPypi,
  buildPythonPackage,
  python-dateutil,
  flask,
  APScheduler,
}:
buildPythonPackage rec {
  pname = "Flask-APScheduler";
  version = "1.12.4";
  format = "setuptools";

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-aB2uNNxsyUA85nR5XlOr0L/1QEchKc/T08k+Dh1QLag=";
  };

  propagatedBuildInputs = [
    python-dateutil
    flask
    APScheduler
  ];
}
