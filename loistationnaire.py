pi = function(p)
{
n  <- dim(p)[1]
q <- t(p)-diag(rep(1,n),n,n)
A = matrix(nrow <- (n+1), ncol <-n)
A[1,] <- rep(1,n)
A[2:(n+1),]<- q
B <-c(1,rep(0,n))
return(qr.solve(A,B))}

P = matrix(c(0,0.5,0.5,1),nrow = 2, ncol=2,byrow = TRUE)

pi(P)