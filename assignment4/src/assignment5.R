library(caret)
library(rpart)
library(tree)
library(randomForest)
library(e1071)
library(ggplot2)
library(rattle)
library(rpart.plot)
library(RColorBrewer)
library(lattice)


# Step 1
seaflow <- read.csv("seaflow_21min.csv")
print(summary(seaflow))

# Step 2
set.seed(142)
trainIdx <- sample(1:nrow(seaflow),nrow(seaflow)/2)
train <- seaflow[trainIdx,]
test  <- seaflow[-trainIdx,]
print(mean(train$time))

# Step 3
print(qplot(pe, chl_small, data=seaflow, color = pop))

# Step 4
fol <- formula( pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small )
modelDTree <- rpart(fol, method="class", data=train)
print(modelDTree)
fancyRpartPlot(modelDTree)

# Step 5
predictionDTree <- predict(modelDTree, test, type = "class")
rateDTree <- sum(predictionDTree==test$pop)/nrow(test)
print(rateDTree)

# Step 6
set.seed(142)
modelRForest <- randomForest(fol, data=train)
predictionRForest <- predict(modelRForest, test, type = "class")
rateRForest <- sum(predictionRForest==test$pop)/nrow(test)
print(rateRForest)
importance(modelRForest)

# Step 7
modelSVM <- svm(fol, data=train)
predictionSVM <- predict(modelSVM, test, type = "class")
rateSVM <- sum(predictionSVM==test$pop)/nrow(test)
print(rateSVM)

# Step 8
table(pred = predictionDTree, true = test$pop)
table(pred = predictionRForest, true = test$pop)
table(pred = predictionSVM, true = test$pop)

# Step 9
# xyplot( chl_small + fsc_perp + pe + fsc_big + fsc_small + chl_big ~ cell_id, data = seaflow)
print(qplot(time, chl_big, data=seaflow, color = pop))
seaflowNew <- seaflow[seaflow$file_id!=208,]

set.seed(142)
trainIdxNew <- sample(1:nrow(seaflowNew),nrow(seaflowNew)/2)
trainNew <- seaflowNew[trainIdxNew,]
testNew  <- seaflowNew[-trainIdxNew,]
modelSVMNew <- svm(fol, data=trainNew)
predictionSVMNew <- predict(modelSVMNew, testNew, type = "class")
rateSVMNew <- sum(predictionSVMNew==testNew$pop)/nrow(testNew)
print(rateSVMNew)



