#include <Mozzi.h>
#include <Oscil.h>
#include <EventDelay.h>
#include <ADSR.h>
#include <tables/sin8192_int8.h>
#include <mozzi_rand.h>
#include <mozzi_midi.h>

Oscil <8192, MOZZI_AUDIO_RATE> aOscil(SIN8192_DATA);;

// for triggering the envelope
EventDelay noteDelay;

ADSR <MOZZI_AUDIO_RATE, MOZZI_AUDIO_RATE> envelope;

boolean note_is_on = true;
boolean footPress=false;
boolean btnPress=false;

int octave = 0;
float freq = 440.0;
float chromatic[13] = {261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370, 392, 412.3, 440, 466.2, 493.9,523.3};
float old[13] = {261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370, 392, 412.3, 440, 466.2, 493.9,523.3};
float scale[8] = {chromatic[0], chromatic[2], chromatic[4], chromatic[5], chromatic[7], chromatic[9], chromatic[11], chromatic[12]};

void setup(){
  //Serial.begin(9600); // for Teensy 3.1, beware printout can cause glitches
  Serial.begin(115200);
  randSeed(); // fresh random
  noteDelay.set(2000); // 2 second countdown
  startMozzi();
	for(int i=22;i<38;i++){
		pinMode(i, INPUT);
	}
}


unsigned int duration, attack, decay, sustain, release_ms;

void updateControl(){
  if(noteDelay.ready()){

      // choose envelope levels
      byte attack_level = 200;
      byte decay_level = 170;
      envelope.setADLevels(attack_level,decay_level);

    // generate a random new adsr time parameter value in milliseconds
     envelope.setTimes(analogRead(0),analogRead(1),analogRead(2),analogRead(3));

		if (digitalRead(53)==HIGH) {
			if (!btnPress) {
				btnPress=true;
				for (int i=0;i<13;i++){
					old[i]=chromatic[i];
				}
				chromatic[12]=old[1]*2;
				chromatic[11]=old[12];
				chromatic[10]=old[11];
				chromatic[9]=old[10];
				chromatic[8]=old[9];
				chromatic[7]=old[8];
				chromatic[6]=old[7];
				chromatic[5]=old[6];
				chromatic[4]=old[5];
				chromatic[3]=old[4];
				chromatic[2]=old[3];
				chromatic[1]=old[2];
				chromatic[0]=old[1];
			}
		} else if (digitalRead(52)==HIGH) {
			if (!btnPress) {
				btnPress=true;
				for (int i=0;i<13;i++){
					old[i]=chromatic[i];
				}
				chromatic[12]=old[11];
				chromatic[11]=old[10];
				chromatic[10]=old[9];
				chromatic[9]=old[8];
				chromatic[8]=old[7];
				chromatic[7]=old[6];
				chromatic[6]=old[5];
				chromatic[5]=old[4];
				chromatic[4]=old[3];
				chromatic[3]=old[2];
				chromatic[2]=old[1];
				chromatic[1]=old[0];
				chromatic[0]=old[11]/2;
			} 
		} else {
			btnPress=false;
		}

		 boolean isPlaying = false;
		 if (!isPlaying) {
			 if (digitalRead(36)==HIGH) {
				 scale[0]=chromatic[1];
			 } else if (digitalRead(37)==HIGH) {
				 scale[0]=chromatic[11]/2;
			 } else {
				 scale[0]=chromatic[0];
			 }
			 if (digitalRead(34)==HIGH) {
				 scale[1]=chromatic[3];
			 } else if (digitalRead(35)==HIGH) {
				 scale[1]=chromatic[1];
			 } else {
				 scale[1]=chromatic[2];
			 }

			 if (digitalRead(32)==HIGH) {
				 scale[2]=chromatic[5];
			 } else if (digitalRead(33)==HIGH) {
				 scale[2]=chromatic[3];
			 } else {
				 scale[2]=chromatic[4];
			 }

			 if (digitalRead(30)==HIGH) {
				 scale[3]=chromatic[6];
			 } else if (digitalRead(31)==HIGH) {
				 scale[3]=chromatic[4];
			 } else {
				 scale[3]=chromatic[5];
			 }

			 if (digitalRead(28)==HIGH) {
				 scale[4]=chromatic[8];
			 } else if (digitalRead(29)==HIGH) {
				 scale[4]=chromatic[6];
			 } else {
				 scale[4]=chromatic[7];
			 }

			 if (digitalRead(26)==HIGH) {
				 scale[5]=chromatic[10];
			 } else if (digitalRead(27)==HIGH) {
				 scale[5]=chromatic[8];
			 } else {
				 scale[5]=chromatic[9];
			 }

			 if (digitalRead(24)==HIGH) {
				 scale[6]=chromatic[12];
			 } else if (digitalRead(25)==HIGH) {
				 scale[6]=chromatic[10];
			 } else {
				 scale[6]=chromatic[11];
			 }

			 if (digitalRead(22)==HIGH) {
				 scale[7]=chromatic[1]*2;
			 } else if (digitalRead(23)==HIGH) {
				 scale[7]=chromatic[11];
			 } else {
				 scale[7]=chromatic[12];
			 }
		 }

		 if (digitalRead(12)==HIGH){
			if (octave>-4 && !footPress) {
				octave--;
				footPress=true;
			}
		 } else if (digitalRead(13)==HIGH){
			if (octave<4 && !footPress) {
				octave++;
				footPress=true;
			}
		 } else {
			footPress=false;
		 }

		 if (digitalRead(2)==HIGH) {
			freq=scale[0]*pow(2,octave);
			isPlaying=true;
		 } else if (digitalRead(3)==HIGH) {
			freq=scale[1]*pow(2,octave);
			isPlaying=true;
		 } else if (digitalRead(4)==HIGH) {
			freq=scale[2]*pow(2,octave);
			isPlaying=true;
		 } else if (digitalRead(5)==HIGH) {
			freq=scale[3]*pow(2,octave);
			isPlaying=true;
		 } else if (digitalRead(6)==HIGH) {
			freq=scale[4]*pow(2,octave);
			isPlaying=true;
		 } else if (digitalRead(8)==HIGH) {
			freq=scale[5]*pow(2,octave);
			isPlaying=true;
		 } else if (digitalRead(9)==HIGH) {
			freq=scale[6]*pow(2,octave);
			isPlaying=true;
		 } else if (digitalRead(10)==HIGH) {
			freq=scale[7]*pow(2,octave);
			isPlaying=true;
		 } else {
			isPlaying=false;
		 }

		 if (isPlaying){
			envelope.noteOn();
		 }
		 else {
			envelope.noteOff();
		 }

     aOscil.setFreq(freq);

		/*
     // print to screen
		 for(int i=0;i<8;i++){
	     Serial.print(i); Serial.println(scale[i]);
		 }
		 */

     noteDelay.start(attack+decay+sustain+release_ms);
   }
}


AudioOutput updateAudio(){
  envelope.update();
  return MonoOutput::from16Bit((int) (envelope.next() * aOscil.next()));
}


void loop(){
  audioHook(); // required here
}