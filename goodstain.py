import sys
import argparse



class HereditaryBaseNumber:

  def __init__(self, value, base):
    self.base = base;
    
    if(value == 0):
      self.components = [];
    else:    
      exponent = 0;
      digits = [];
      while value > 0:
        digits.append((value % base, exponent));
        exponent +=1;
        value /= base;
        
      digits = [(d,e) for (d,e) in digits if d != 0];
      self.components = [(d, HereditaryBaseNumber(e, base)) for (d,e) in reversed(digits)];
      
      
  def val(self):
    return sum([d*(self.base)**e.val() for d,e in self.components]);
      
  def _coeficient(self, d):
    return "" if d==1 else str(d)+".";
    
  def _term(self, base, e):
    if e.val() == 0:
      return "1"
    elif e.val() == 1:
      return str(b)
    else:
      return "%s^{%s}" %(b, str(e));
  
  def __str__(self):
    if(self.val() <= self.base):
      return str(self.val());
    return " + ".join(["%s%s" % (self._coeficient(d), self._term(self.base, e)) for (d, e) in self.components]);
    
      
  def increaseBase(self):
    self.base +=1;
    for (_, e) in self.components:
      e.increaseBase();
  
    
def goodstainNext(k):
  pass
  
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Generates a Goodstain sequence.')
    parser.add_argument('-s', type=int,  default=13, help="Starting number. (default: 13)")
    parser.add_argument('-n', type=int, default=10, help="Number of iterations to compute. (default: 10)");
    args = parser.parse_args();
  
    s = args.s
    b = 2
    k = HereditaryBaseNumber(s,b);
    for i in range(args.n):
      print("$$ %s = %s $$"  % (str(k.val()), str(k)))
      k.increaseBase();
      s = k.val()-1;
      b += 1;
      k = HereditaryBaseNumber(s,b);
    
