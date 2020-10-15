#comentariu
x <-  11

#y = 1 # nu e indicat sa facem atribuire cu =

print("Uite mama fara dinti")
 #ctrl + enter pentru a rula linia curenta

a <- c(1, 2, 8) #vector cu 3 elem

b <- -5 : 15 


c <- 4.9 : 10.3

d <- seq(0, 4*pi, 0.001) #genereaza in interval dens

d[4]


sin (0)

sin(d)

plot(d, sin(d), col = "magenta") # doar grafic

plot(d, sin(d), col = "magenta", ylim = c(-5, 5), xlim = c(0,2)) #limitam graficul pe intervale
plot(d, sin(d), col = "magenta",xlim = c(0,5*pi)) #limitam graficul pe intrvale



length(log (b[b>0])) #valorile din b care sunt pozitive


log (b[((b > 0) & (b %% 2 == 0)) | (b %% 3 == 0)])
            # |

a + b[1:3] # aduna a cu primele valori din b


a + b # cand dimnesiunea vect mai mic divide dim vect mai mare
      # a se prelungeste cu aceleasi valori


v <- 6 : 105
