# encoding: utf-8
'''Interface com a ANAC'''

import logging
import re
from netrc import netrc
from mechanize import Browser


def _log():
    if not _log.logger:
        _log.logger = logging.getLogger()
    return _log.logger
_log.logger = None


class Anac(object):

    def __init__(self, dryrun):
        self.dryrun = dryrun
        self.br = Browser()
        self.br.set_handle_robots(False)
        self.br.open('https://sistemas.anac.gov.br/SACI/')
        self.br.select_form(nr=0)
        self.host = 'sistemas.anac.gov.br'
        a = netrc().authenticators(self.host)
        if a is None:
            _log().error('Usuario e senha para %s não encontrado no ~/.netrc' % self.host)
        self.br.form['txtLogin'] = a[0]
        self.br.form['txtSenha'] = a[2]
        r = self.br.submit()
        m = re.search("(\/SACI\/CIV\/Digital\/incluir\.asp[^']+)'", r.read())
        self.url = 'https://' + self.host + m.group(1)

    def add(self, dat):
        self.br.open(self.url)
        self.br.select_form(nr=0)
        self.br.form.set_all_readonly(False)
        for k, v in dat.items():
            self.br.form[k] = v
        _log().debug('Dados do formulário: ' + str(self.br.form))
        if self.dryrun:
            _log().warn('dryrun')
            return
        r = self.br.submit().read()
        if 'sucesso' in r:
            return
        _log().warn(r)



