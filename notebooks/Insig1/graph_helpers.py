import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
import mpld3

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

def gen_pairwise_sequence_identities(dbsequence, dbsca):
    
    Dseq = dbsequence[0]
    Dsca = dbsca[0]

    pairwiseSeqID_list = [Dsca['simMat'][i,j] for i in range(Dsca['simMat'].shape[0]) 
         for j in range(i+1, Dsca['simMat'].shape[1])]
    
    plt.rcParams['figure.figsize'] = 10,6
    plt.figure()
    binsize = int(round(Dseq['Npos']/2)) #half of the number of positions
    plt.hist(pairwiseSeqID_list,bins =binsize, color = 'navy')
    avgSID = np.mean(pairwiseSeqID_list)
    plt.plot([avgSID,avgSID],[0,70000],'--r',linewidth = 2)
    plt.text(avgSID+0.05,50000,str(round(avgSID*100,2))+'% mean pair-wise sequence similarity',fontsize=12,color = 'darkred')
    plt.xlabel('pairwise sequence identities')
    plt.ylabel('number of sequences')
    plt.xlim(0,1.1)

def gen_eigenvalues_graph(dbsequence, dbsca, dbsector):

    Dseq = dbsequence[0]
    Dsca = dbsca[0]
    Dsect = dbsector[0]
    print('Number of eigenmodes to keep is %i' %(Dsect['kpos']))
    plt.rcParams['figure.figsize'] = 9, 4
    hist0, bins = np.histogram(Dsca['Lrand'].flatten(), bins=Dseq['Npos'], \
                            range=(0,Dsect['Lsca'].max()))
    hist1, bins = np.histogram(Dsect['Lsca'], bins=Dseq['Npos'], \
                            range=(0,Dsect['Lsca'].max()))
    plt.bar(bins[:-1], hist1, np.diff(bins),color='k')
    plt.plot(bins[:-1], hist0/Dsca['Ntrials'], 'r', linewidth=3)
    plt.tick_params(labelsize=11)
    plt.xlabel('Eigenvalues', fontsize=18); plt.ylabel('Numbers', fontsize=18);

def gen_sig_eigennodes_graphs(dbsector):

    Dsect = dbsector[0]

    plt.rcParams['figure.figsize'] = 9, 6

    pairs = []
    kpos = int(Dsect['kpos'])
    for pos in range(1,kpos-1):
        pairs.append([pos-1,pos])

    EVs = Dsect['Vsca']
    ICs = Dsect['Vpica']
    for k,[k1,k2] in enumerate(pairs):
        #we're not compensating for the additional eigenmodes properly here
        plt.subplot(2,3,k+1)
        plt.plot(EVs[:,k1], EVs[:,k2], 'ok')
        plt.xlabel("EV%i"%(k1+1), fontsize=16)
        plt.ylabel("EV%i"%(k2+1), fontsize=16)
        plt.subplot(2,3,k+4)
        plt.plot(ICs[:,k1], ICs[:,k2], 'ok')
        plt.xlabel("IC%i"%(k1+1), fontsize=16)
        plt.ylabel("IC%i"%(k2+1), fontsize=16)
    plt.show()