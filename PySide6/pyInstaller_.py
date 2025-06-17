# Para empacotar programa em um arquivo executável do sistema (um app)
# pip install pyinstaller

# Para verificar o caminho absoluto do arquivo (RAIZ):
# python -c 'import pathlib; print(pathlib.Path().absolute())';

# C:\Users\NAJA INFORMATICA\Desktop\Udemy\Aulas_Python\Pyside6

# No Terminal 
# APLICAÇÃO:
# pyinstaller --name="CalculadoraPython" --noconfirm --onefile 
# --add-data="..\Calculadora\files\;files\" --icon="..\Calculadora\files\icon.png"
# --noconsole --clean --log-level=WARN Calculadora\main.py

# Para escolher onde salvar a aplicação, acrescentar:
# --distpath="nomepasta/dist" --workpath="nomepasta/build" 
# --specpath="nomepasta/" Calculadora\main.py
