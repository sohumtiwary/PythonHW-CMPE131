class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def shape(self):
        # uses the subclass name so this works for other shapes too
        return f"This is a {self.__class__.__name__.lower()}"


class Circle(Base):
    def __init__(self, x, y, size):
        # correct parameters
        super().__init__(x, y, size)

    def draw(self):
        return f"""({self.x}, {self.y})
{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """


def main():
    c = Circle(1, 2, 3)
    print(c.shape()) 
    print(c.draw())


if __name__ == "__main__":
    main()
