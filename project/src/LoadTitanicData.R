

trainOriginal <- read.csv("train.csv");
testOriginal  <- read.csv("test.csv");
testOriginal$Survived <- NA

titanicOriginal <- rbind(trainOriginal,testOriginal)

titanicOriginal$Name  <- as.character(titanicOriginal$Name)
titanicOriginal$Title <- sapply(titanicOriginal$Name, FUN=function(x) {strsplit(x, split='[,.]')[[1]][2]})
titanicOriginal$Title <- sub(' ', '', titanicOriginal$Title)

titanicOriginal$Title[titanicOriginal$Title %in% c('Mme', 'Mlle')] <- 'Mlle'
titanicOriginal$Title[titanicOriginal$Title %in% c('Capt', 'Don', 'Major', 'Sir')] <- 'Sir'
titanicOriginal$Title[titanicOriginal$Title %in% c('Dona', 'Lady', 'the Countess', 'Jonkheer')] <- 'Lady'
titanicOriginal$Title <- factor(titanicOriginal$Title)


avgAgesPerTitle <- aggregate(Age ~ Title, data=titanicOriginal, FUN=mean)
titanicOriginal[is.na(titanicOriginal$Age),"Age"] <- sapply(titanicOriginal[is.na(titanicOriginal$Age),"Title"], function(a) {
        idx <- which(avgAgesPerTitle[,"Title"]==a)
        avgAgesPerTitle[idx,"Age"]
    } 
    )


avgFaresPerTitle <- aggregate(Fare ~ Title, data=titanicOriginal, FUN=mean)
titanicOriginal[is.na(titanicOriginal$Fare),"Fare"] <- sapply(titanicOriginal[is.na(titanicOriginal$Far),"Title"], function(a) {
    idx <- which(avgFaresPerTitle[,"Title"]==a)
    avgFaresPerTitle[idx,"Fare"]
} 
)


titanicOriginal$Child <- 0
titanicOriginal$Child[titanicOriginal$Age < 18] <- 1

titanicOriginal$FamilySize <- titanicOriginal$SibSp + titanicOriginal$Parch + 1
titanicOriginal$Surname <- sapply(titanicOriginal$Name, FUN=function(x) {strsplit(x, split='[,.]')[[1]][1]})
titanicOriginal$FamilyID <- paste(as.character(titanicOriginal$FamilySize), titanicOriginal$Surname, sep="")
titanicOriginal$FamilyID[titanicOriginal$FamilySize <= 2] <- 'Small'
titanicOriginal$FamilyID <- factor(titanicOriginal$FamilyID)

train <- titanicOriginal[1:nrow(trainOriginal),]
test  <- titanicOriginal[(nrow(trainOriginal)+1):(nrow(trainOriginal)+nrow(testOriginal)),]


