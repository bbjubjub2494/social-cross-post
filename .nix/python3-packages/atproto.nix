{
  lib,
  fetchPypi,
  buildPythonPackage,
  poetry-core,
  poetry-dynamic-versioning,
  click,
  dacite,
  websockets,
  pyjwt,
  dag-cbor,
  httpx,
  multiformats,
}:
buildPythonPackage rec {
  pname = "atproto";
  version = "0.0.24";
  format = "pyproject";

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-3aoIkyaP5BviJ4vuvzVikLxU1ntnxeCf9q6NKhg7wno=";
  };

  propagatedBuildInputs = [
    poetry-core
    poetry-dynamic-versioning
    click
    dacite
    websockets
    pyjwt
    dag-cbor
    httpx
    multiformats
  ];
}
