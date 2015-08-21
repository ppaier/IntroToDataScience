library(party)
source("LoadTitanicData.R")

set.seed(1)

fit <- cforest(as.factor(Survived) ~ Fare + Pclass + Sex + Age + Title + FamilySize + Child, 
               data=train, controls=cforest_unbiased(ntree=2000, mtry=3))

prediction <- predict(fit, test, OOB=TRUE, type = "response")
submit <- data.frame(PassengerId = test$PassengerId, Survived = prediction)

write.csv(submit, file = "solution2.csv", row.names = FALSE)
