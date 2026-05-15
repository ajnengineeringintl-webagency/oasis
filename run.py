from app import server
oasapp=server()
if __name__ == "__main__":
  oasapp.run(debug=True,port=4208,host="localhost")