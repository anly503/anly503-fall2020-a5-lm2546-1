library(plotly)
library(ggplot2)
library(dplyr)

#Change the work file directory to be same as the R file location.
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))


#Read data
data<-read.csv("eco/cleaned_data2.csv")
data$Month<-factor(data$Month, levels = c('July','August','September','October','November','December','All'))


# Set up the pie plot factos.
plot<-plot_ly(data, labels=~Part,values=~Consumption,type='pie',frame=~Month,
              marker=list(colors=c("#8ffaff", "#78ff59", "#ff9156",'#eb56ff',
                                   '#abb1ab','#ff5967','#460202','#074239')),
              textinfo='label+percent',
              textposition='inside',
              insidetextfont=list(color = '#FFFFFF'),
              hoverinfo='text',
              text=~paste(Part,'\n',Consumption, ' Millions'),
              marker=list(colors=colors,line=list(color='#FFFFFF',width=1)),showlegend=T)
plot <- plot %>% layout(title = 'Percentage of Each Part Electricity Cosumption(Millions)',font=T,
                        xaxis = list(showgrid=FALSE,zeroline=FALSE,showticklabels=FALSE),
                        yaxis = list(showgrid=FALSE,zeroline=FALSE,showticklabels=FALSE))

plot <- plot %>%  animation_slider(
  currentvalue = list(prefix = "Month: ", font = list(color="#010203"))
)

plot
#Save Plot to local File
htmlwidgets::saveWidget(as_widget(plot), "docs/plotly.html")

