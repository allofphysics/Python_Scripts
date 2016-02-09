

complete <- function(directory='specdata',id=1:332){
  tf<- data.frame()
  files <- list.files()[id]
  for(x in files){df <- do.call(rbind,lapply(x,read.csv)) 
  df<-df[complete.cases(df),]
  var<-c(as.numeric(unlist(strsplit(x,'\\.'))[1]),dim(df)[1])
  tf <- rbind(tf,var)
  
  }
  names(tf) <- c('id','nobs')
  tf
}
df<-complete("specdata", 1:332)

corr <- function(directory='specdata',threshold =0) {
  test <- data.frame()
  vec<-c(which(df['nobs']>threshold))
  files<-list.files()[vec]
  for(f in files){
    tf<-read.csv(f)
    tf<-tf[complete.cases(tf),]
    test1<-cor(tf['sulfate'],tf['nitrate'])
    test<-rbind(test,test1)
  } 
  head(test)
  summary(test)
  }
corr('specdata',150)
