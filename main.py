import sys
from app.aplicacao import Aplicacao
def main() -> int:
    return Aplicacao().executar()

if __name__ == "__main__":
    sys.exit(main())
