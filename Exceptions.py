class Tramwaj:
  def __init__ (self, typ, numer):
    self.typ = typ
    self.numer = numer
  def __str__ (self):
    return f'Jestem tramwajem typu {self.typ} o numerze {self.numer}'
  
class Zajezdnia:
  def __init__ (self, lista_tramwajow):
    self.lista_tramwajow = lista_tramwajow
  def __add__ (self, tramwaj):
    if type(tramwaj) != Tramwaj:
      raise TypeError(f'Argument {tramwaj} nie jest klasą Tramwaj')
    else:
      self.lista_tramwajow.append(tramwaj)
      return self
  def __sub__ (self, tramwaj):
    if type(tramwaj) != Tramwaj:
      raise TypeError(f'Argument {tramwaj} nie jest klasą Tramwaj')
    elif tramwaj not in self.lista_tramwajow:
      raise ValueError(f'Argument {tramwaj} nie znajduje sie na liscie')
    self.lista_tramwajow.remove(tramwaj)
    return self
  def wypiszTramwaje (self):
    print(f'Obecnie w zajezdni znajduja sie:')
    for x in self.lista_tramwajow:
      print(x)


  
zajezdnia_nowa_huta = Zajezdnia([])
tramwaj1 = Tramwaj('krakowiak', 5)
tramwaj2 = Tramwaj('konstal', 12)
tramwaj3 = Tramwaj('akwarium', 13)

zajezdnia_nowa_huta = zajezdnia_nowa_huta + tramwaj1
zajezdnia_nowa_huta = zajezdnia_nowa_huta + tramwaj2
zajezdnia_nowa_huta = zajezdnia_nowa_huta
zajezdnia_nowa_huta.wypiszTramwaje()

zajezdnia_nowa_huta = zajezdnia_nowa_huta - tramwaj1
zajezdnia_nowa_huta = zajezdnia_nowa_huta - tramwaj1

zajezdnia_nowa_huta.wypiszTramwaje()