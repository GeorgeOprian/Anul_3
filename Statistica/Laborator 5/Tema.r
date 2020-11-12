#Gama
e_natural <- function(n){
  return ((n %% 1 == 0)  && (n > 0)) 
}
fg <- function (x, a){
  x ^ (a - 1) * exp(-x)
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
  
  
  #prod = 1
  #while (n >= 1) {
  #  prod = prod * (n - 1)
  #  n = n - 1
  #}
  if (n>=1) {
    print ("folosesc proprietatea 2 si integrate")
    return ((n - 1) * gama_nume(n - 1)* integrate(fg, 0, Inf, a = n)$value)
  }
  return (1)
}



#Poisson


gen_val <- function (i, lambda){
  return ((exp(-lambda) * lambda^i)/factorial(i))
}

gen_Val_poisson <- function(n, lamda){
  rez <- vector()
  for (i in 1:n){
    rez = c(rez, gen_val(i,lamda))
  } 
  return (rez)
}

gen_val_poisson_algoritm <- function(lambda){
  u <- runif(1)
  p <- exp(-lambda) 
  F <- p
  i <- 0
  while (u>F) {
    p <- (lambda*p)/(i+1)
    F = F + p
    i = i + 1
  }
  x = i
  return (x)
}



gen_Val_poisson(10, 4)

