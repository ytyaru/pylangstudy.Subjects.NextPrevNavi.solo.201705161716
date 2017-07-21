#eval "$(rbenv init -)"
#export PATH="~/.pyenv/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"

rbenv exec asciidoctor index.adoc

