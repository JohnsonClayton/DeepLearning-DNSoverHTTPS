# Get the libraries needed
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the input file
datafile = open('results_nov23.txt', 'r')
lines = datafile.readlines()

# Set up the dataframe
df = pd.DataFrame()
df['name'] = pd.Series(dtype=str)
df['Accuracy_avg'] = pd.Series(dtype=float)
df['Accuracy_std'] = pd.Series(dtype=float)
df['Precision_avg'] = pd.Series(dtype=float)
df['Precision_std'] = pd.Series(dtype=float)
df['Recall_avg'] = pd.Series(dtype=float)
df['Recall_std'] = pd.Series(dtype=float)
df['AUC_avg'] = pd.Series(dtype=float)
df['AUC_std'] = pd.Series(dtype=float)
df['exp_time'] = pd.Series(dtype=float)
df['n_features'] = pd.Series(dtype=int)

# Set up variables we need
name = ''
acc_avg = 0
acc_std = 0
rec_avg = 0
rec_std = 0
prec_avg = 0
prec_std = 0
auc_avg = 0
auc_std = 0
exp_time = 0
n_features = 0

for line in lines:
    # Remove the new lines
    line = line.strip()

    # Split up by spaces
    line_arr = list( filter( None, line.split(' ') ) )

    # Let us know which line we are about to parse
    #print('parsing...{}'.format(line_arr))

    # Don't do anything if we aren't on a row with data
    if len(line_arr) > 2:
        # Check if we are in a new table
        if line_arr[0] == 'Running' and line_arr[-1] != 'you?':
            n_features = int(line_arr[4])
            exp_time = float(line_arr[8])
        # If the line starts with an sklearn learner, then use the data from the line!
        elif line_arr[0].split('.')[0] == 'sklearn':
            # Assign the name of the classifier we are working with
            if len(line_arr) == 5:
                # Then the name of the classifier is in the first element
                name = line_arr[0].split('.')[-1]
            elif len(line_arr) > 5:
                # Then the first two elements are the names
                name = (' '.join(line_arr[:2])).split('.')[-1]

            if name == 'Gaussian':
                name = 'gaussian naive\nbayes'
            elif name == 'Linear':
                name = 'linear discriminant  \nanalysis'
            elif name == 'extreme gradient':
                name = 'extreme gradient   \nboosting'

            # Extract the data from the line
            data = line_arr[-4:]

            acc_avg = float(data[0].split('\u00B1')[0])
            acc_std = float(data[0].split('\u00B1')[1])

            rec_avg = float(data[1].split('\u00B1')[0])
            rec_std = float(data[1].split('\u00B1')[1])

            prec_avg = float(data[2].split('\u00B1')[0])
            prec_std = float(data[2].split('\u00B1')[1])

            auc_avg = float(data[3].split('\u00B1')[0])
            auc_std = float(data[3].split('\u00B1')[1])

            # Set up the row for the dataframe
            new_row = {
                'name':name,
                'Accuracy_avg':acc_avg,
                'Accuracy_std':acc_std,
                'Recall_avg':rec_avg,
                'Recall_std':rec_std,
                'Precision_avg':prec_avg,
                'Precision_std':prec_std,
                'AUC_avg':auc_avg,
                'AUC_std':auc_std,
                'exp_time':exp_time,
                'n_features':n_features
            }

            #print(new_row)

            # Add the new row to the dataframe object
            df = df.append( new_row, ignore_index=True )

        else:
            name = ''

datafile.close()

# Use the dataframe to produce the graphs

# Show the experiment time as we increase the number of features
# As this is right now, this is not a valuable metric because of the settings it was run under
#plt.figure()
#sns.lineplot(
#    x='n_features',
#    y='exp_time',
#    data=df
#)
#plt.show()

# Produce the graph with error bars
    
plt.rcParams.update({'font.size':25})
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True)
fig.set_size_inches(18, 12)

i = 0
j = 0
metrics = ['Accuracy', 'Recall', 'Precision', 'AUC']
for metric in metrics:
    # Show the accuracy for each model as we increase the number of features
    #plt.figure()
    ax = axes[i][j] #plt.axes()
    i += 1
    if i == 2:
        i = 0
        j += 1

    # Set up the y limits for the graph (each one may require a little tweaking)
    if metric == 'Accuracy':
        ax.set_ylim(0.4, 1.0)
    elif metric == 'Recall':
        ax.set_ylim(0.4, 1.0)
    elif metric == 'Precision':
        ax.set_ylim(0.7, 1.0)
    elif metric == 'AUC':
        ax.set_ylim(0.7, 1.0)

    # For every model name in the dataframe
    for name in df['name'].unique():
        df_tmp = df.loc[ df['name'] == name ]

        # Plot the data
        ax.plot(
            df_tmp['n_features'],
            df_tmp['{}_avg'.format(metric)],
            label=name
        )

        # Plot the error bars
        #   Graph with a shaded line everything in-between (x, y1) and (x, y2)
        ax.fill_between(
            x=df_tmp['n_features'],

            # Everything within the standard deviation above the mean
            y1=df_tmp['{}_avg'.format(metric)] + df_tmp['{}_std'.format(metric)],

            # Everything within the standard deviation below the mean
            y2=df_tmp['{}_avg'.format(metric)] - df_tmp['{}_std'.format(metric)],

            # This affects the opacity of the line (0 => really light, 1 => really bold)
            alpha=0.15
        )

    # Set up the legend
    handles, labels = ax.get_legend_handles_labels()
    lgd = fig.legend(
        handles, labels, 
        loc='center right', 

        # We are using this to position the legend outside of the plots
        bbox_to_anchor=(1.25, 0.50), 

        # This turns the border of the legend off
        frameon=False
        )

    # Set the labels on the graph
    if i == 0:
        ax.set_xlabel('Top N Features')
    ax.set_ylabel(metric)
fig.tight_layout()

# Save the figure. We can show it with `plt.show()`, but it doesn't look as pretty and the
#  legend is not showing up correctly. However, it saves the image correctly.
fig.savefig('nov23results_err', bbox_inches='tight')

# Produce the graph without error bars
    
plt.rcParams.update({'font.size':25})
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True)
fig.set_size_inches(18, 12)

i = 0
j = 0
metrics = ['Accuracy', 'Recall', 'Precision', 'AUC']
for metric in metrics:
    # Show the accuracy for each model as we increase the number of features
    #plt.figure()
    ax = axes[i][j] #plt.axes()
    i += 1
    if i == 2:
        i = 0
        j += 1

    # Set up the y limits for the graph (each one may require a little tweaking)
    if metric == 'Accuracy':
        ax.set_ylim(0.4, 1.0)
    elif metric == 'Recall':
        ax.set_ylim(0.4, 1.0)
    elif metric == 'Precision':
        ax.set_ylim(0.7, 1.0)
    elif metric == 'AUC':
        ax.set_ylim(0.7, 1.0)

    # For every model name in the dataframe
    for name in df['name'].unique():
        df_tmp = df.loc[ df['name'] == name ]

        # Plot the data
        ax.plot(
            df_tmp['n_features'],
            df_tmp['{}_avg'.format(metric)],
            label=name
        )

    # Set up the legend
    handles, labels = ax.get_legend_handles_labels()
    lgd = fig.legend(
        handles, labels, 
        loc='center right', 

        # We are using this to position the legend outside of the plots
        bbox_to_anchor=(1.25, 0.50), 

        # This turns the border of the legend off
        frameon=False
        )

    # Set the labels on the graph
    if i == 0:
        ax.set_xlabel('Top N Features')
    ax.set_ylabel(metric)
fig.tight_layout()

# Save the figure. We can show it with `plt.show()`, but it doesn't look as pretty and the
#  legend is not showing up correctly. However, it saves the image correctly.
fig.savefig('nov23results_noerr', bbox_inches='tight')
