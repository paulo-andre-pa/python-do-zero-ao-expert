class ErroBiblioteca(Exception):
    """Base de todos os erros do domínio."""

class NaoEncontrado(ErroBiblioteca):
    pass

class LivroIndisponivel(ErroBiblioteca):
    pass

class LimiteAtingido(ErroBiblioteca):
    pass

class SocioImpedido(ErroBiblioteca):
    pass

class EmprestimoDuplicado(ErroBiblioteca):
    pass
