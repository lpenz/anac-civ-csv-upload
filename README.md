[![Build Status](https://travis-ci.org/lpenz/anac-civ-csv-upload.svg?branch=master)](https://travis-ci.org/lpenz/anac-civ-csv-upload)
[![Coverage Status](https://coveralls.io/repos/lpenz/anac-civ-csv-upload/badge.svg)](https://coveralls.io/r/lpenz/anac-civ-csv-upload)

# anac-civ-csv-upload

Utilitário que envia uma planilha como rascunho para o CIV digital da ANAC.

Você pode exportar a planilha para CSV a partir do Excel. Campos necessários:
- dia: formato ano-mes-dia;
- matricula: da aeronave, que é marcada sempre como planador (aceito patch!);
- origem,destino: código dos aeródromos;
- reb,plan,duplo,solo: tempo, em minutos, de reboque, planado, com o total solo ou duplo.


O utilitário considera que o cadastro é como aluno se o voo for duplo. O
cadastro é sempre de voo visual.

O arquivo exemplo-civ.csv possui um exemplo de planilha. Campos adicinais são ignorados.

A configuração de usuário e senha é feita no ~/.netrc:
    machine sistemas.anac.gov.br
    login <usuario>
    password <senha>

O certificado SSL da anac não é válido nos sistemas que testei, vai ser
necessário instalá-lo. Não consegui fazer isso, e acabei usando as instruções
em https://github.com/hurzl/mechanize/commit/f34dcc6f5aac219d9483303a98668dc213465925
para ignorar este problema.


