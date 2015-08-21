
library(e1071)
source("LoadTitanicData.R")

fit <- svm(as.factor(Survived) ~ Fare + Pclass + Sex + Age + Title + FamilySize + Child + Parch + Embarked + SibSp, data = train)
x2 <- subset(test, select = c(Fare,Pclass,Sex,Age,Title,FamilySize,Child,Parch,Embarked,SibSp))

prediction <- predict(fit, x2)
submit <- data.frame(PassengerId = test$PassengerId, Survived = prediction)

write.csv(submit, file = "solution3.csv", row.names = FALSE)
