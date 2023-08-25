from setuptools import setup

setup(name='social-cross-post',
      version='1.0',
      description='x-post to Bluesky, Mastodon, Posthaven, Instagram, and, ugh, Twitter',
      url='https://github.com/GanWeaving/social-cross-post',
      author='GanWeaving',
      include_package_data=True,
      install_requires=[
          'pytz',
          'Pillow',
          'Flask',
          'Flask-Session',
          'Flask-APScheduler',
          'Flask-SQLAlchemy',
          'atproto',
          'requests',
          'Mastodon.py',
          'tweepy',
          'requests-oauthlib',
          ],
      )
