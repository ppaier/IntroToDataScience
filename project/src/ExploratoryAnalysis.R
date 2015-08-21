
source("LoadTitanicData.R")
#pairs(train)

#train <- train[train$Sex=="male",]

randNoise <- rnorm(nrow(train),0,0.01) 

with(train, plot(Age, Survived, main = "Titanic", type = "n"))

points(train$Age[train$Survived==1],as.numeric(train$Survived[train$Survived==1])+
         randNoise[train$Survived==1], col="blue")

points(train$Age[train$Survived==0],as.numeric(train$Survived[train$Survived==0])+
         randNoise[train$Survived==0], col="red")


with(train, plot(Fare, Sex, main = "Titanic", type = "n"))

points(train$Fare[train$Survived==1],as.numeric(train$Sex[train$Survived==1])+
           randNoise[train$Survived==1], col="blue")

points(train$Fare[train$Survived==0],as.numeric(train$Sex[train$Survived==0])+
           randNoise[train$Survived==0], col="red")


with(train, plot(Age, Pclass, main = "Titanic", type = "n"))

points(train$Age[train$Survived==1],as.numeric(train$Pclass[train$Survived==1])+
           randNoise[train$Survived==1], col="blue")

points(train$Age[train$Survived==0],as.numeric(train$Pclass[train$Survived==0])+
           randNoise[train$Survived==0], col="red")


