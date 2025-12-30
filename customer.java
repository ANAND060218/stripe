public class M{
    public int compute_penalty(String log,int close){
        int penalty=0;
        for(int i=0;i<log.length();i++){
            if(i<close && log.charAt(i)=='N'){
                penalty+=1;
            }
            else if(i>=close && log.charAt(i)=='Y'){
                penalty+=1;
            }
        }
        return penalty;

    }
    public int getClosingWithMinPenalty(String log){
        int curr=0;
        int time=0;
        int n=log.length();
        int close=curr;
        for(int i=0;i<n;i++){
            char c=log.charAt(i);
            if(c=='Y')curr--;
            else curr++;
            if(curr<close){time=i+1;close=curr;}

        }
        return time;


    }
    public int getAllClosing(String log){
        String[] logs=log.split(" ");
        Stack<StringBuilder>stack=new Stack<>();
        ArrayList<Integer>res=new ArrayList<>();
        for(String i:logs){
            if(i=="B"){ stack.push(new StringBuilder());}
            else if(i=="E"){
                if(!stack.isEmpty()){
                    String s=stack.pop.toString();
                    res.add(getClosingWithMinPenalty(s));
                }
            }
            else{stack.peek().append(i); }
        }
    

    }





    public static void main(String[] args) {

    }}
