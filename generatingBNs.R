library(bnlearn)

d <- read_csv("~/Desktop/phd/code/tortLaw/tort_extended.csv", 
                            col_types = cols(X1 = col_skip(), cau = col_factor(), 
                                                    dmg = col_factor(), duty = col_factor(), 
                                                        ico = col_factor(), ift = col_factor(), 
                                                        ila = col_factor(), jus = col_factor(), 
                                                        prp = col_factor(), vrt = col_factor(), 
                                                        vst = col_factor(), vun = col_factor(),
                                                        c1 = col_factor(), c2 = col_factor(),
                                                        c3 = col_factor(), c4 = col_factor(),
                                                        c5 = col_factor()
                                                  ))


d <- as.data.frame(d)

structure <- hc(d)
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/bic.net", fitted)
plot(structure)


structure <- hc(d, score="loglik")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/loglik.net", fitted)
plot(structure)


structure <- hc(d, score="aic")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/aic.net", fitted)
plot(structure)

structure <- hc(d, score="bdj")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/bdj.net", fitted)
plot(structure)

structure <- hc(d, score="pred-loglik")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/predloglik.net", fitted)
plot(structure)

structure <- hc(d, score="bde")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/bde.net", fitted)
plot(structure)

structure <- hc(d, score="bds")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/bds.net", fitted)
plot(structure)

structure <- hc(d, score="mbde")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/mbde.net", fitted)
plot(structure)

structure <- hc(d, score="bdla")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/bdla.net", fitted)
plot(structure)

structure <- hc(d, score="k2")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/k2.net", fitted)
plot(structure)

structure <- hc(d, score="fnml")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/fnml.net", fitted)
plot(structure)

structure <- hc(d, score="qnml")
fitted = bn.fit(structure, d, method = "mle")
write.net(file="~/Desktop/phd/code/tortLaw/automaticBNs/qnml.net", fitted)
plot(structure)

