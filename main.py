import java.util.ArrayList
from java.util import ArrayList

java.util.ArrayList == ArrayList

al = ArrayList()
al.add(1)
al.add(12)
print(al)
# prints [1, 12]

import java
BigInteger = java.type("java.math.BigInteger")
myBigInt = BigInteger.valueOf(42)
# public Java methods can just be called
myBigInt.shiftLeft(128)
# Java method names that are keywords in Python can be accessed using `getattr`
getattr(myBigInt, "not")()
byteArray = myBigInt.toByteArray()
# Java arrays can act like Python lists
print(list(byteArray))
