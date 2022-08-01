import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt


def onewaysummary(df_input, xvars, target, exposure, boo_stack=False):
    """
    returns a dictionary of univariate summary dataframes or a stacked single dataframe (based on boo_stack)
    inputs:
        df_input (dataframe)
        xvars (list of strings)
        target (string)
        exposure (string) used as denom of target
        boo_stack (boolean) whether to stack the output into a single dataframe. best for excel charts.
    """
    dict_summary = {}
    # create dictionary of summaries
    for i in range(len(xvars)):
        dict_summary[i] = df_input[[xvars[i]] + [exposure] + [target]].groupby(by=xvars[i]).sum().reset_index()
        dict_summary[i]['freq'] = dict_summary[i][target] / dict_summary[i][exposure]

    if boo_stack:
        for i in range(len(dict_summary)):
            # format before append
            dict_summary[i].insert(0, 'variable', dict_summary[i].columns[0])
            dict_summary[i].rename(columns={dict_summary[i].columns[1]: 'level1'}, inplace=True)

        stack = pd.concat(dict_summary, ignore_index=True, axis=0)
        return stack
    else:
        return dict_summary


def onewayplot(df_input, barvar, linevar):
    """
    plots a stacked dataframe of univariate summaries
    inputs:
        df_input (dataframe)
        barvar (string)
        linevar (string)
    """

    myfontsize = 7
    ls_variables = df_input['variable'].unique().tolist()

    # initialize figure.
    ncols = 5
    nrows = max(math.ceil((len(ls_variables) / ncols)), 2)
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols)

    i = 0
    for currrow in range(nrows):
        for currcol in range(ncols):

            # check if you've exhausted the variable list first.
            if i < len(ls_variables):
                # update the variable name.
                currvar = ls_variables[i]

                # filter for the variable of interest.
                plotdata = df_input.loc[df_input['variable'] == currvar].reset_index(drop=True)

                # set title
                axs[currrow, currcol].set_title(currvar, fontsize=myfontsize)

                # manipulate first axis.
                axs[currrow, currcol].bar(plotdata['level1'].astype('category'), plotdata['rec'], color='slategrey')
                axs[currrow, currcol].xaxis.set_tick_params(labelsize=myfontsize, rotation=45)
                axs[currrow, currcol].set_ylabel('records', fontsize=myfontsize)
                axs[currrow, currcol].yaxis.set_tick_params(labelsize=myfontsize)

                # manipulate second axis.
                ax2 = axs[currrow, currcol].twinx()
                ax2.plot(plotdata['level1'].astype('category'), plotdata['freq'], color='firebrick', marker='.')
                ax2.set_ylabel('freq', fontsize=myfontsize)
                ax2.yaxis.set_tick_params(labelsize=myfontsize)

                # show it.
                plt.show()

                # increment variable index.
                i += 1









