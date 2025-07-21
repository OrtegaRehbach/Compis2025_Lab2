from SimpleLangListener import SimpleLangListener
from SimpleLangParser import SimpleLangParser
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckListener(SimpleLangListener):

  def __init__(self):
    self.errors = []
    self.types = {}

  def enterMod(self, ctx: SimpleLangParser.ModContext):
    pass

  def exitMod(self, ctx: SimpleLangParser.ModContext):
    left  = self.types[ctx.expr(0)]
    right = self.types[ctx.expr(1)]

    if isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
      self.types[ctx] = FloatType() if isinstance(left, FloatType) or isinstance(right, FloatType) else IntType()
    else:
      self.errors.append(f"Unsupported operand types for %: {left} and {right}")

  def enterMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    pass

  def exitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for * or /: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def enterAddSub(self, ctx: SimpleLangParser.AddSubContext):
    pass

  def exitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    op = ctx.op.text
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    
    if op == '+':
      if isinstance(left_type, StringType) and isinstance(right_type, (StringType, IntType, BoolType)):
        self.types[ctx] = StringType()
        return
      if isinstance(left_type, StringType) or isinstance(right_type, StringType):
        self.errors.append(f"Cannot add {left_type} and {right_type}")
        return
    
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for + or -: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def enterPow(self, ctx: SimpleLangParser.PowContext):
    pass

  def exitPow(self, ctx: SimpleLangParser.PowContext):
    left  = self.types[ctx.expr(0)]
    right = self.types[ctx.expr(1)]

    if isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
      self.types[ctx] = FloatType()
    else:
      self.errors.append(f"Unsupported operand types for ^: {left} and {right}")
  
  def enterInt(self, ctx: SimpleLangParser.IntContext):
    self.types[ctx] = IntType()

  def enterFloat(self, ctx: SimpleLangParser.FloatContext):
    self.types[ctx] = FloatType()

  def enterString(self, ctx: SimpleLangParser.StringContext):
    self.types[ctx] = StringType()

  def enterBool(self, ctx: SimpleLangParser.BoolContext):
    self.types[ctx] = BoolType()

  def enterParens(self, ctx: SimpleLangParser.ParensContext):
    pass

  def exitParens(self, ctx: SimpleLangParser.ParensContext):
    self.types[ctx] = self.types[ctx.expr()]

  def is_valid_arithmetic_operation(self, left_type, right_type):
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return True
    return False
