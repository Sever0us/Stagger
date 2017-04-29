from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2'
]

setup(name='stagger',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = stagger:main
      """,
)