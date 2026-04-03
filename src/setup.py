from setuptools import setup
import setup_translate

pkg = 'Extensions.FritzCall'
setup(name='enigma2-plugin-extensions-fritzcall',
       version='3.0',
       description='Show Incoming and Outgoing Calls on your TV Screen with a Fritz!Box',
       package_dir={pkg: 'FritzCall'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'plugin.png', 'reverselookup.xml', 'LICENSE', 'maintainer.info', 'callbycall_world.xml', 'avon.dat', 'images/MODERN/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
