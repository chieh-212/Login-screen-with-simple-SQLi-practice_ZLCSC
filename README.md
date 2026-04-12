  This is a simple lab for ZLCSC course, 
  including SQLi, SSTi and IDOR

  
  SQLi part: Login screen  
  just pay attention to the IF and use `'OR 1=1 --`
  so that you can log in as admin and see the flag

  SSTi part: search  
  use 'search' to find the product you want to buy...haha, the funcion just trick, you can't find the products including those key words!
  try to combine the payload with `config`, `__init__`, `__globals__`, `__builtins__`, `__import__`, `os`, `read()`

  IDOR part: products  
  just observe the URL

  there's also a flag hidden in a path that can't be crawled. 
  Five flags in total, have fun:)
