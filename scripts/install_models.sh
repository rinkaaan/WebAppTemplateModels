WORKPLACE="$HOME/workplace/WebAppTemplate"

(
  cd "$WORKPLACE/WebAppTemplateModels"
  pip install .
  rm -rf build
)
