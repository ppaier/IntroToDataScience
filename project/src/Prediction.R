
library(rpart)
source("LoadTitanicData.R")

trainMale   <- train[train$Sex=="male",]
trainFemale <- train[train$Sex=="female",]

testMale   <- test[test$Sex=="male",]
testFemale <- test[test$Sex=="female",]

fitMale   <- rpart(Survived ~ Pclass + Age + SibSp, data=trainMale,   method="class")
fitFemale <- rpart(Survived ~ Pclass + Age + Fare, data=trainFemale, method="class")

PredictionMale <- predict(fitMale, testMale, type = "class")
submitMale <- data.frame(PassengerId = testMale$PassengerId, Survived = PredictionMale)

PredictionFemale <- predict(fitFemale, testFemale, type = "class")
submitFemale <- data.frame(PassengerId = testFemale$PassengerId, Survived = PredictionFemale)

submit <- rbind(submitMale,submitFemale)
write.csv(submit, file = "myfirstdtree.csv", row.names = FALSE)
