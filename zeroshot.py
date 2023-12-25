from ZSIC import ZeroShotImageClassification
zsic = ZeroShotImageClassification()

emotions=["happy","sad","anger","neutral","suprise","disgust","fear"]
gender=["male","female"]

def emotion_pred(filename):
	print(filename)
	emotion_preds=zsic(image=filename,candidate_labels=emotions)
	gender_preds=zsic(image=filename,candidate_labels=gender)
	return(max(emotion_preds["scores"]),emotion_preds["labels"][emotion_preds["scores"].index(max(emotion_preds["scores"]))],max(gender_preds["scores"]),gender_preds["labels"][gender_preds["scores"].index(max(gender_preds["scores"]))])