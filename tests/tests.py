#!/usr/bin/env python

import os
import imp
import shutil
import os.path
import tempfile
import unittest
import urllib

os.chdir(os.path.dirname(__file__))

mpac = imp.load_source("mpac", "../mpac")

mpac.URPMI_DATA_DIR = '.'
mpac.URPMI_CONFIG_FILE = 'urpmi.cfg'

g_urpmi_config = mpac.UrpmiConfig()

MIRROR_BASE_URL = 'http://mirrors.kernel.org/mageia/distrib/2/x86_64/'

for m in g_urpmi_config.parse():
    fname = 'synthesis.hdlist.%s.cz' % m.name
    print m.name
    if not os.path.exists(fname):
        urllib.urlretrieve(MIRROR_BASE_URL
                           + '/media/media_info/'
                           + fname.replace('hdlist.', 'hdlist_'), fname)

class TestCommand(unittest.TestCase):
    def setUp(self):
        self._tempdir = tempfile.mkdtemp()
        mpac.DATABASE_FILE = os.path.join(self._tempdir, 'mpac.sqlite3')
        db = mpac.init_database()
        self.media = mpac.Media(db)

        for m in g_urpmi_config.parse():
            self.media.append(m)
        self.media.update_db()

    def test_cmd_install(self):
        cmd = mpac.CmdInstall(self.media)
        self.assertIsNone(cmd._cmd(['in', 'ff']))
        self.assertEqual(cmd._cmd(['in', 'ffmpeg'])[:3],
                         ['urpmi', '--searchmedia', 'tainted_updates'])

    def test_cmd_refresh(self):
        cmd = mpac.CmdRefresh(self.media)
        self.assertEqual(cmd._cmd(['nonfree_updates']),
                         ['urpmi.update', 'nonfree_updates'])
        self.assertEqual(cmd._cmd([]),
                         ['urpmi.update', 'tainted_updates',
                          'nonfree_release', 'nonfree_updates'])
        self.assertEqual(cmd._cmd(['-A']),
                         ['urpmi.update', 'tainted_release',
                          'debug_tainted_release', 'tainted_updates',
                          'nonfree_release', 'nonfree_updates'])

    def test_cmd_update(self):
        cmd = mpac.CmdUpdate(self.media)
        self.assertEqual(cmd._cmd([]), ['urpmi', '--auto-update'])
        self.assertEqual(cmd._cmd(['-R']), ['urpmi', '--auto-select'])

    def test_cmd_list(self):
        enabled = mpac.CmdList(self.media)._list(self.media.enabled, False)
        all_media = mpac.CmdList(self.media)._list(self.media, False)
        all_enabled = mpac.CmdList(self.media)._list(self.media.enabled, True)
        all_media_enabled = mpac.CmdList(self.media)._list(self.media, True)

        self.assertTrue(len(enabled) < len(all_enabled))
        self.assertTrue(len(enabled) < len(all_media))
        self.assertTrue(len(all_enabled) < len(all_media_enabled))

    def tearDown(self):
        shutil.rmtree(self._tempdir)

if __name__ == '__main__':
    unittest.main()
