install.packages("igraph")
library("igraph")


data <- edit(data.frame())
E(g)$weight = data$var3
#empezamos a usar igraph --------------
g  <- graph.data.frame(data, directed = FALSE)    # Crea igraph
class(g)                                          # Clase del objeto
V(g)$name                                         # Nombres de los vertices 
E(g)$weight                                       # Peso de las aristas
tkplot(g)                                         # Grafico dinamico 
plot(g, edge.label = paste(E(g)$weight, sep= "")) # Grafico de abajo
