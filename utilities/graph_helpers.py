import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch

def gen_amino_acid_position_in_ref_sequence_graph(
    xlabel = "No title passed as arg",
    ylabel = '$D_{i}$',
    bar_color='navy',
    di_threashold_color='cyan',
    fontsize=18,
    figwidth=18,
    figheight=6,
    Dsca = [],
    Dseq = [],
):
    plt.rcParams['figure.figsize'] = figwidth,figheight
    yData = Dsca[0]['Di']
    xData = np.arange(len(yData))
    xData1 = Dseq[0]['ats']
    xData1 = [float(i) if type(i) is not str else i for i in xData ]
    plt.bar(xData,yData,color = bar_color,edgecolor = 'none')

    plt.xlabel(xlabel,fontsize=fontsize)
    plt.ylabel(ylabel,fontsize=fontsize)

    #X labels for subset of positions. Needed to do this otherwise, the figure is too crowded. 
    xticklocations = np.arange(0,len(xData1),10) 
    xtickPosLabels = [Dseq[0]['ats'][a] for a in xticklocations]
    plt.xticks(xticklocations,xtickPosLabels)

    #Plots threshold for Di in cyan. Should see some positions where it drops below 0.5 for a sufficient diversity across positions. 
    plt.plot([-10,len(Dseq[0]['ats'])+10],[0.5,0.5],'--',color = di_threashold_color,linewidth = 2)

    #Set min and max axes of figure 
    plt.xlim(-2, len(Dseq[0]['ats']))
    plt.ylim(0,4)

def _data_clusterer(Dsca, method='complete', metric='cityblock'):
    Z = sch.linkage(Dsca[0]['simMat'],method = method, metric = metric)
    R = sch.dendrogram(Z,no_plot = True)
    ind = R['leaves']
    return Z,R,ind

def gen_unclustered_similarity_matrix(
    title = "No title passed as arg",
    Dsca = [],
    data_cluster_method='complete', 
    data_cluster_metric='cityblock',
    interpolation='nearest',
    cmap='bwr'
):
    Z,R,ind = _data_clusterer(Dsca,data_cluster_method,data_cluster_metric)
    plt.figure()
    plt.title(title)
    plt.imshow(Dsca[0]['simMat'],interpolation = 'nearest',cmap = 'bwr',vmin = 0,vmax = 1) 

def gen_clustered_similarity_matrix(
    title = "No title passed as arg",
    Dsca = [],
    data_cluster_method='complete', 
    data_cluster_metric='cityblock',
    interpolation='nearest',
    cmap='bwr'
):
    Z,R,ind = _data_clusterer(Dsca,data_cluster_method,data_cluster_metric)
    plt.figure()
    plt.title('Clustered')
    plt.imshow(Dsca[0]['simMat'][np.ix_(ind,ind)],vmin = 0,vmax = 1, cmap = 'bwr',interpolation = 'nearest')
    plt.colorbar()