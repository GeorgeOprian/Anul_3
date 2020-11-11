#Gama
e_natural <- function(n){
  return ((n %% 1 == 0)  && (n > 0)) 
}

gama_nume <- function (n) {
  if (n == 1) {
    print ("folosesc proprietatea 1")
    return (1)
  }
  if (e_natural(n)) {
    print ("folosesc proprietatea 3")
    return (factorial(n - 1))
  }
  if (n == 1/2){
    print (c("folosesc proprietatea 4", n))
    return (sqrt(pi))
  }
  if (e_natural(n - 1/2)){
    print (c("folosesc proprietatea 2", n))
    return ((n - 1) * gama_nume(n - 1))
  }
  prod = 1
  while (n >= 1) {
    prod = prod * (n - 1)
  }
  print ("folosesc proprietatea 2 si integrate")
  return (integrate(prod))
}



#Poisson

gen_Var_poisson <- function(lambda){1
  U = runif(1)
  i = 0
  p = exp((-1) * lambda)
  F = p
  while (U >= F){
    p = (lambda * p)/(i + 1)
    i = i+ 1
    F = F + p
  }
  return (c(p, i))
}

gen_Val_poisson <- function(n, lamda){
  rez <- vector()
  for (i in 1:n){
    rez = c(rez, gen_Var_poisson(lamda)[1])
  } 
  return (rez)
}


gen_Val_poisson(10, 4)