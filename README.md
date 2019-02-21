# Jupyter notebook Style Helper

## What is, the purpose of this project?
This is style generator, you can simply generate inline css to insert into your Jupyter notebook to change look of tables in your preview.

## How to install:
Just copy files from "code" directory to your project and import it. In **Demo** directory you can find examples 

## What python version is required?
Code is compatible with python >= 3.5

## How to use it?
```python
from IPython.display import HTML, display
import seaborn as sns
from Code import StyleHelper

style_generator = StyleHelper.StyleHelper()
style_generator.emit_style()

iris = sns.load_dataset('iris')
display(iris.head(5))
```

## Show me the change in style
TBD

## How can I customise generated style?
 * **col_header_color** - Column header color
 * **row_header_color** - Row header color
 * **selector** - css selector to apply style only to selected elements

## ToDo:
* Prepare pip package
* Add parameters for: lines, margins, shadows, etc.
* Add a support for predefined themes 


