import tensorflow as tf

# loading the model
model = tf.keras.models.load_model('../../models/model.keras')

# taking the user input
sms = input("Enter the Message (SMS) you received: ")
text = tf.constant([sms])

prediction = model.predict(text) # predicting through the model

# final verdict
if prediction[0][0] >= .5 :
    print("It is a Spam Message. Kindly Ignore it.")
    print(f"I am {round(prediction[0][0], 2)*(100)}% sure.")
else:
    print("It is a Ham Message. Do care to read it.")
    print(f"I am {(1 - round(prediction[0][0], 2))*100}% sure.")