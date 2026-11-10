CONFIGURADOR FF — BUILD PELO CELULAR

Este pacote contém o projeto e um workflow que compila o APK em um servidor
do GitHub Actions. Assim, você pode iniciar a compilação pelo navegador do
Android, sem instalar o compilador Android no celular.

PASSOS:
1. Crie uma conta no GitHub, se ainda não tiver.
2. Crie um repositório novo e público chamado configurador-ff.
3. Extraia este ZIP no celular e envie os arquivos/pastas para a raiz do
   repositório, incluindo a pasta .github/workflows.
4. No repositório, abra Actions e selecione "Build Android APK".
5. Toque em Run workflow e confirme.
6. Quando terminar com sucesso, abra a execução e baixe o artefato
   "configurador-ff-apk". O ZIP do artefato contém o APK.

Observação: o Termux não é o caminho oficial/simples para compilar Kivy APK.
Este projeto é um configurador independente: ele salva sugestões de
sensibilidade no próprio app e não modifica nem controla o Free Fire.
