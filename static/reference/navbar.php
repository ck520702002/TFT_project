<?php session_start();?>
<style>
  li#login-name{
    padding: 15px;
    color:white;
  }
  .navbar-right{
    margin-right: 30px !important;
  }
</style>
<div class="navbar-wrapper">
      <div class="container">

        <div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="./index.php">IM web</a>
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="active"><a href="./index.php">Home</a></li>
                <?php if(empty($_SESSION["sid"])){?>
                  </ul>
                <?php }else{?>
				<li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">查詢<b class="caret"></b></a>
                  <ul class="dropdown-menu">
                    <li><a href="student_infor.php">個人資料</a></li>
					<li><a href="#">修課狀況</a></li>
				  </ul>
				</li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">參加<b class="caret"></b></a>
                  <ul class="dropdown-menu">
                    <li><a href="act_join.php?type=sa">系學會</a></li>
					<li><a href="act_join.php?type=team">系隊</a></li>
				  </ul>
				</li>  
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">報名 <b class="caret"></b></a>
                  <ul class="dropdown-menu">
                    <li><a href="act_join.php?type=activity">活動</a></li>
                    <li><a href="act_join.php?type=game">比賽</a></li>
                    <li><a href="act_join.php?type=party">導生宴</a></li>
                  </ul>
                </li>
              </ul>
              <?php }?>
			  <ul class="nav navbar-nav navbar-right">
<?php if(empty($_SESSION["sid"])){?>
				<li><a href="regi.php">註冊</a></li>
				<li><a href="login.php">登入</a></li>
<?php }else{?>
        <li id="login-name"><?php echo "Hi~ ";if(empty($_SESSION["name"]))echo "無名氏";else echo $_SESSION["name"];?></li>
        <li><a href="logout.php">登出</a></li>  <!-- -->
<?php } ?>
        </ul>
            </div>
          </div>
        </div>

      </div>
    </div>