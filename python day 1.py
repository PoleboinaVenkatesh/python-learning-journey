{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e169f408-abb1-4a06-b2be-50ccd17577b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'helloworld!'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"helloworld!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "482b3a19-22dc-4411-a690-e8ac40a901aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helloworld!\n"
     ]
    }
   ],
   "source": [
    "print(\"helloworld!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "423ac588-b293-497a-ac82-d6fe4f36decb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'test'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"helloworld!\"\n",
    "\"test\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cf277c7a-e4d3-4a62-a3e6-07706a290563",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helloworld!\n",
      "test\n"
     ]
    }
   ],
   "source": [
    "print(\"helloworld!\")\n",
    "print(\"test\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "175844ea-1fb0-4123-9426-f2671191ac48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function print in module builtins:\n",
      "\n",
      "print(*args, sep=' ', end='\\n', file=None, flush=False)\n",
      "    Prints the values to a stream, or to sys.stdout by default.\n",
      "\n",
      "    sep\n",
      "      string inserted between values, default a space.\n",
      "    end\n",
      "      string appended after the last value, default a newline.\n",
      "    file\n",
      "      a file-like object (stream); defaults to the current sys.stdout.\n",
      "    flush\n",
      "      whether to forcibly flush the stream.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(print)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c5407e8f-e73e-45ae-bdf4-7f2ff0a79eae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helloworld!\n"
     ]
    }
   ],
   "source": [
    "print(\"helloworld!\",flush=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b54a983b-21aa-4ccd-bb10-dc72b98e325b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "gfkzjgfgxjftsjkfjzcfdfjvekbfssmgfjsfurfgvbvfv7trglqwfuwfid\n"
     ]
    }
   ],
   "source": [
    "print(\"gfkzjgfgxjftsjkfjzcfdfjvekbfssmgfjsfurfgvbvfv7trglqwfuwfid\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6fc23ea6-965e-4c32-be9b-b6627213089f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helloworld!test"
     ]
    }
   ],
   "source": [
    "print(\"helloworld!\",end=\"\")\n",
    "print(\"test\",end=\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5ac0bb1b-4989-4ca2-b989-204adb397e75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helloworld!  test  a  b  "
     ]
    }
   ],
   "source": [
    "print(\"helloworld!\",end=\"  \")\n",
    "print(\"test\",end=\"  \")\n",
    "print(\"a\",end=\"  \")\n",
    "print(\"b\",end=\"  \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b020a025-cb07-4960-a9d3-301af131052d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3\n",
      "4 5 6\n",
      "7 8 9\n"
     ]
    }
   ],
   "source": [
    "print(1,2,3)\n",
    "print(4,5,6)\n",
    "print(7,8,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "37014f21-a0e6-4672-8108-e9601eeded9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1   2   3   4   5\n",
      "6   7   8   9   10\n",
      "11   12   13   14   15\n"
     ]
    }
   ],
   "source": [
    "print(\"1\",end=\"   \")\n",
    "print(\"2\",end=\"   \")\n",
    "print(\"3\",end=\"   \")\n",
    "print(\"4\",end=\"   \")\n",
    "print(5)\n",
    "print(\"6\",end=\"   \")\n",
    "print(\"7\",end=\"   \")\n",
    "print(\"8\",end=\"   \")\n",
    "print(\"9\",end=\"   \")\n",
    "print(\"10\")\n",
    "print(\"11\",end=\"   \")\n",
    "print(\"12\",end=\"   \")\n",
    "print(\"13\",end=\"   \")\n",
    "print(\"14\",end=\"   \")\n",
    "print(\"15\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fbe4d322-c0fb-4023-9f5a-1d4123efad76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  _ _ _ _ _\n",
      "| VENKATESH |\n",
      "  _ _ _ _ _\n"
     ]
    }
   ],
   "source": [
    "print(\" \",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\")\n",
    "print(\"|\",end=\" \")\n",
    "print(\"VENKATESH\",end=\" \")\n",
    "print(\"|\")\n",
    "print(\" \",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\",end=\" \")\n",
    "print(\"_\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ddc2184a-59f8-4590-b59c-31de830f0635",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'int'>,<class 'float'>\n",
      "<class 'bool'>,<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "print(type(\" \"))\n",
    "print(type(2),end=\",\")\n",
    "print(type(4.4))\n",
    "print(type(True),end=\",\")\n",
    "print(type(False))\n",
    "           \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "364d32e3-dae3-4c37-8063-e250104f6f8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(\"6\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "6e1274e0-b503-48fc-8319-7feeeeb786b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.0"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "float(\"6\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3f44eacb-2ec6-4efb-af9e-c238b4b771dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool(\"2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "e7183bd3-224b-48d5-b9ee-bbc2b4e41c2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool(int(0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "f1c8d992-a6f2-4d56-9c51-18e93534582e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool(float(-6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "e00f7e25-261e-4055-9f7c-a8e047d37566",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "55ac1a82-b7c1-43f6-aa21-e2ecf1d49ad9",
   "metadata": {},
   "outputs": [],
   "source": [
    "b=3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "46992f04-0a03-4c95-88cb-71bff88aac81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "44\n"
     ]
    }
   ],
   "source": [
    "b=b+1\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "36114b01-e6f8-4891-9f95-842f81ce6d6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "h=43"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "6b949169-2d9a-4383-8f17-a7c7ea418ccc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n"
     ]
    }
   ],
   "source": [
    "h=h-1\n",
    "print(h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "736ae19e-ac4e-4323-b62a-a2d84a6be338",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "75\n",
      "74\n",
      "73\n",
      "72\n",
      "71\n",
      "70\n",
      "69\n",
      "68\n"
     ]
    }
   ],
   "source": [
    "h=75\n",
    "print(h)\n",
    "h=h-1\n",
    "print(h)\n",
    "h=h-1\n",
    "print(h)\n",
    "h=h-1\n",
    "print(h)\n",
    "h=h-1\n",
    "print(h)\n",
    "h=h-1\n",
    "print(h)\n",
    "h=h-1\n",
    "print(h)\n",
    "h=h-1\n",
    "print(h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "c8894a58-d3f2-4b0d-b97b-20b90f816941",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "67\n",
      "68\n",
      "69\n",
      "70\n",
      "71\n",
      "72\n",
      "73\n",
      "74\n",
      "75\n",
      "76\n"
     ]
    }
   ],
   "source": [
    "a=67\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)\n",
    "a=a+1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adf9e15b-ad58-4025-a7cc-2d0f7da77f09",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
