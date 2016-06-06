import random, sys

def create(number, file_products, file_result):
   f = open(file_products, 'r')
   p = open(file_result, 'w')
   l = [i.strip('\n') for i in f]

   t = 0.0
   for i in range(0, number):
      b = float(random.randint(0, 100))
      c = float(round(random.uniform(0.25, 10), 2))
      t += b * c
      a = random.choice(l) + ' ' + str(b) + ' ' + str(c) + '\n'
      p.write(a)

   print("Total -> %0.2f" % t)
   
if __name__ == '__main__':
   create(int(sys.argv[1]), sys.argv[2], sys.argv[3])