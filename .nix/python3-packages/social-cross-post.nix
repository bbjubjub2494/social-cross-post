{
  buildPythonPackage,
  pytz,
  pillow,
  requests,
  tweepy,
  mastodon-py,
  flask-session,
  flask-sqlalchemy,
  atproto,
  Flask-APScheduler,
}:
buildPythonPackage {
  pname = "social-cross-post";
  version = "1.0-unstable";
  src = ../..;
  format = "pyproject";

  propagatedBuildInputs = [
    pytz
    pillow
    requests
    tweepy
    mastodon-py
    flask-session
    flask-sqlalchemy
    atproto
    Flask-APScheduler
  ];
}
