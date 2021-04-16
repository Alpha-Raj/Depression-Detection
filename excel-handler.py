import os
import pandas as pd
from data_preprocessing import preprocess

# Directory which will hold the transcripts.csv file of all the participants
DIRECTORY = "data"
PARTICIPANT = "Participant"
GROUND_TRUTH_FILE = "dev_split_Depression_AVEC2017.csv"
Participant_ID = "Participant_ID"
PHQ8_Score = "PHQ8_Score"


def get_gt_value(gt_file, participant_id):
    """
    function which will accept the participant id and Ground Truth File and
    will return its respective ground truth
    :param gt_file: Ground truth File Handler
    :param participant_id: Participant Id
    :return: ground truth value
    """
    for index, row in gt_file.iterrows():
        pid = row['Participant_ID']
        if str(pid) == participant_id:
            y_train = row['PHQ8_Score']
            return y_train
    print("Ground Truth for " + participant_id + " Not Found")
    return -1


def open_and_extract():
    data = []
    files = [os.path.join(DIRECTORY, file) for file in os.listdir(DIRECTORY)]
    gt_file = pd.read_csv(GROUND_TRUTH_FILE, sep=',')
    for file in files:
        participant_id = file.split("/")[1].split("_")[0]
        y_train = get_gt_value(gt_file, participant_id)
        if y_train != -1:  # All the participants whose GT is Absent will not be considered.
            x_train = ""
            df = pd.read_csv(file, sep='\t')
            for index, row in df.iterrows():
                if row['speaker'] == PARTICIPANT:
                    value = row['value']
                    x_train = x_train + " " + value
            print("Data found Participant Id:" + participant_id)
            data.append([preprocess(x_train), y_train])
    data_df = pd.DataFrame(data, columns=[Participant_ID, PHQ8_Score])
    data_df.to_csv("Dev-Data", sep=',', index=False)


if __name__ == '__main__':
    print("****** File reading Process Started ******")
    open_and_extract()
    print("****** File reading Process Started ******")
